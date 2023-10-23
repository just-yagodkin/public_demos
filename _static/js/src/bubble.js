import *  as c from './constants';

let angle = -Math.PI / 2;
let initial_angle = angle;

export class Bubble {
    constructor(p) {
        this.p = p;
        // this.speed = speed;
        this.col = this.p.color(255, 100, 76);
        this.diameter = 25;
        this.strokeweight = 1;
        this.strokecolor = 'black'
        this.counter = 0
        this.info = false
    }


    display() {
        this.counter += 1
        if (this.info === true) {
            if (this.counter % 20 < 10) {
                this.p.stroke(this.strokecolor);
                this.p.strokeWeight(this.strokeweight);
                this.p.fill(this.col);
            } else {
                this.p.stroke('black');
                this.p.strokeWeight(1);
            }

        } else {
            this.p.stroke(this.strokecolor);
            this.p.strokeWeight(this.strokeweight);
            this.p.fill(this.col);
        }
        this.x = c.centerX + c.radius * this.p.cos(angle);
        this.y = c.centerY + c.radius * this.p.sin(angle);
        this.p.ellipse(this.x, this.y, this.diameter, this.diameter);
        this.p.fill('black');
        this.p.noStroke();
        this.p.ellipse(this.x, this.y, 5, 5);
        angle = angle + speed;
    }
    set_to_start() {
        angle = initial_angle;
    }
    change_bubble_shape(strokecolor, strokeweight) {
        this.strokeweight = strokeweight;
        this.strokecolor = strokecolor;
    }


    is_within_arc(arc) {
        this.p.translate(c.canv_size / 2, c.canv_size / 2);
        let a = this.p.atan2(this.y - c.canv_size / 2, this.x - c.canv_size / 2);
        let corr = this.x - c.canv_size / 2 < 0 && this.y - c.canv_size / 2 < 0;
        a = corr === false ? a : Math.PI * 2 + a;
        return (arc.start_angle < a && a < arc.end_angle);

    }
};
