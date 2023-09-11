//TODO: move bubbles and arcs into sep class and export using require, module.export
import p5 from "./p5";
import {Bubble} from './bubble';
import {Arc, ChoosableArc} from './arc';
import *  as c from './constants';
import jspsych from "./jspsych";

let bubble,
    game,
    arcs = [];

const s = (p) => {
    let chosen_arc;
    p.setup = function () {
        p.createCanvas(c.canv_size, c.canv_size);
        bubble = new Bubble(p);
        c.arc_lengths.forEach((i, j) => {
            let start_angle = j === 0 ? 0 : arcs[j - 1].uncorrected_angles.end;
            let end_angle = start_angle + i;
            let color = c.colors[j];
            let A = choose_difficulty === true ? ChoosableArc : Arc;
            let t = new A({
                p: p,
                end_angle: end_angle,
                col: color,
                chosen: false,
                start_angle: start_angle,
                id: j,
                transparency: 255,
            });
            arcs.push(t);
        });
        if (choose_difficulty === false) {
            chosen_arc = arcs[chosen_arc_id];
            chosen_arc.chosen = true;
        }
    };

    p.draw = function () {
        p.background('green');
        p.stroke(1);
        p.strokeWeight(1);
        p.noFill();
        p.ellipse(c.centerX, c.centerY, c.diameter);
        bubble.display();
        arcs.forEach((i, j) => {
            i.display();
        })

    };
    let event_happened = () => {
        let in_canvas = (p.mouseX > 0 && p.mouseX < c.canv_size && p.mouseY > 0 && p.mouseY < c.canv_size);
        if (in_canvas) {
            if (choose_difficulty === true) {
                arcs.forEach((i, j) => {
                    if (i.is_clicked()) {
                        arcs.forEach((l, m) => {
                            l.chosen = false
                        });
                        i.chosen = true;
                        i.do_if_clicked();
                    }
                });
            } else {


                arcs.forEach(l => l.set_transparency(80));
                let old_speed = speed;
                speed = 0;

                bubble.change_bubble_shape('red', 4)
                bubble.info = true;
                $('#id_task').val((bubble.is_within_arc(chosen_arc) === true) ? 1 : 0);
                setTimeout(function () {
                    $('form#form').submit();
                }, 3000);
            }
        }
    }
    p.mousePressed = () => {
        jspsych(new Date());
        event_happened();
    };
    p.touchEnded = () => {
        event_happened();
    }
};
let deliver_game = () => {
    $('#id_task').val(game);
    // $('#form').submit();
}
let myp5 = new p5(s, 'p5cont');
