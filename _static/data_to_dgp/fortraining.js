
var cy = cytoscape({
  container: document.getElementById('cy'),

  boxSelectionEnabled: false,
  autounselectify: true,

  style: cytoscape.stylesheet()



    .selector('node')
      .css({
        'content': 'data(name)',
        'text-valign': 'center',
        'color': 'black',
        // 'text-outline-width': 2,
        // 'text-outline-color': undefined,
        'background-color': '#666'
      })
    .selector(':selected')
      .css({
        'background-color': 'black',
        'line-color': 'black',
        'target-arrow-color': 'black',
        'source-arrow-color': 'black',
        'text-outline-color': 'black'
      })
    .selector('edge')
      .css({
        'width': 2,
        'line-color': '#ccc',
        'target-arrow-color': 'black',
        'target-arrow-shape': 'triangle',
        'curve-style': 'bezier',
        'line-style': 'dashed'
      })
      .selector('edge[label]')
      .css({
        "label": "data(label)",
        "width": 3
      })
      .selector('layout')
      .css({
        'name': 'grid',
        'rows': 1,
        'cols': 2,
        'padding': 15,
      })
      ,




  elements: {
    nodes: [
      // { style: {'border-color': "red"}, data: {counter:0, id: 'a', name: '-', } },
      { data: {counter:0, id: 'X', name: 'X', }, style: { 'background-color': '#c3cec0' } },
      { data: {counter:0, id: 'Y', name: 'Y', },  style: { 'background-color': '#c3cec0' }},
      { data: {counter:0, id: 'Z', name: 'Z', },  style: { 'background-color': '#c3cec0' }},
      // { data: {counter:0, id: 'Z', name: '-', } }
    ],
    edges: [
      { data: {counter:0, weight:0, id: 'XY', source: 'X', target: 'Y', label: ""} },
      { data: {counter:0, weight:0, id: 'YX', source: 'Y', target: 'X', label: ""} },
      { data: {counter:0, weight:0, id: 'YZ', source: 'Y', target: 'Z' , label: ""} },
      { data: {counter:0, weight:0, id: 'XZ', source: 'X', target: 'Z' , label: ""} },
      { data: {counter:0, weight:0, id: 'ZY', source: 'Z', target: 'Y' , label: ""} },
      { data: {counter:0, weight:0, id: 'ZX', source: 'Z', target: 'X' , label: ""} },
      // { data: {counter:0, weight:0, id: 'bc', source: 'Y', target: 'Z', label: "-"} },
    ]
  },


});

var layout = cy.layout({
  name: 'circle'
});

layout.run();

const edge_states = ["",""];
const edge_colours = ["#ccc","#000"]
const edge_type = ['dashed','solid' ]
const edge_weight = [2,0]



cy.on('tap', 'edge', function(evt){
  var ele = evt.target;
  var edges = cy.edges();
  var form_data = [];
  // console.log(iterator(numbers, ele.data('counter'))[0] );
  ele.data('label', iterator(edge_states, ele.data('counter'))[0]);
  ele.data('counter', iterator(edge_states, ele.data('counter'))[1]);
  ele.data('weight', iterator(edge_weight, ele.data('counter'))[0]);
  ele.style('line-style', edge_type[ele.data('counter')] );
  ele.style('line-color', edge_colours[ele.data('counter')] );
  for (var i = 0; i < edges.length; i++) {
    form_data.push(edges[i]._private.data);
  }
  console.log(form_data);
  liveSend(form_data);
  // sendValue(form_data)
  form_data = [];
});

function liveRecv(data) {
      // forminputs.trainig.value = data;
      formInputs.trainig.value = data; // for server setting
      console.log(data)
  }



function iterator(array, i) {
  var index=(i+1)% array.length;
  var value = array[index];

    return [value, index];
  };
