//TODO: move bubbles and arcs into sep class and export using require, module.export
import p5 from "./p5";
import {Bubble} from './bubble';
import {Arc, ChoosableArc} from './arc';
import *  as c from './constants';
import jspsych from "./jspsych";

let bubble,
    arc;
const s = (p) => {

    p.setup = function () {
        p.createCanvas(c.canv_size, c.canv_size);
        bubble = new Bubble(p);

        arc = new ChoosableArc(p,6, 145,150);

    };

    p.draw = function () {
        p.background(255);
        p.stroke(1);
        p.strokeWeight(1);
        p.noFill();
        p.ellipse(c.centerX, c.centerY, c.diameter);
        bubble.display();
        arc.display();
    };
    p.mousePressed = function () {
        jspsych(new Date());
        bubble.clicked();
        arc.clicked();
    };
};

let myp5 = new p5(s, 'p5cont');
