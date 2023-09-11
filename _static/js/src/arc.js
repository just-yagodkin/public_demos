import {SQUARE, PI, OPEN} from "./p5";
import *  as c from './constants';
import * as p from 'script-loader!./p5.js';

let start_angle = 0,
    width = 30;

export class Arc {
    constructor({
                    p, start_angle = 0,
                    transparency = c.arc_transparency,
                    end_angle,
                    radius = c.radius,
                    col,
                    chosen = false,
                    id = undefined
                }) {
        this.id = id;
        this.p = p;
        this.uncorrected_angles = {'start': start_angle, 'end': end_angle};
        let levels = p.color(col).levels;
        levels[3] = transparency;
        this.centerX = c.centerX;
        this.centerY = c.centerY;
        this.start_angle = start_angle + c.correction;
        this.end_angle = end_angle + c.correction;
        this.col = p.color(levels);
        this.width = width;
        this.radius = radius;
        this.chosen = chosen;
        this._is_clicked = false;
    }


    display() {
        this.p.stroke(this.col);
        this.p.strokeWeight(this.width);
        this.p.strokeCap("butt");
        this.p.noFill();
        this.p.arc(this.centerX, this.centerY, this.radius * 2, this.radius * 2, this.start_angle, this.end_angle, p.OPEN);
        if (this.chosen) {

            this.p.stroke('black');
            this.p.strokeWeight(2);
            this.p.arc(this.centerX, this.centerY, this.radius * 2 - this.width, this.radius * 2 - this.width, this.start_angle, this.end_angle, p.OPEN);
            this.p.arc(this.centerX, this.centerY, this.radius * 2 + this.width, this.radius * 2 + this.width, this.start_angle, this.end_angle, p.OPEN);
        }

    }

    is_clicked() {
        return (this._is_within_width() && this._is_within_angles());
    }

    _is_within_width() {
        let d = this.p.dist(this.p.mouseX, this.p.mouseY, this.centerX, this.centerY);
        let lb = this.radius - this.width / 2;
        let ub = this.radius + this.width / 2;
        return (d >= lb && d <= ub);
    }

    _is_within_angles() {
        let innerangle = this.p.atan2(this.p.mouseY - this.centerY, this.p.mouseX - this.centerX);
        if (innerangle < c.correction) {
            innerangle = 2 * Math.PI + innerangle;
        }
        return (innerangle >= this.start_angle && innerangle <= this.end_angle);
    }

    set_transparency(alpha) {
        let p = this.p;
        let col = this.col
        let levels = p.color(col).levels;
        levels[3] = alpha;
        this.col = p.color(levels);
    }

    do_if_clicked() {
        console.log('arc clicked!');
    }

    clicked() {
        this._is_clicked = this.is_clicked();
        if (this.is_clicked()) {
            this.do_if_clicked();

        }
        ;
        return this;
    };
};

export class ChoosableArc extends Arc {
    do_if_clicked() {
        super.do_if_clicked();
        $('#id_difficulty').val(this.id);

    }
}