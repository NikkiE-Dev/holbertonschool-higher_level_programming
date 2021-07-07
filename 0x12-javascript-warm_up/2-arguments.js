#!/usr/bin/node
const process = require('process');
let resp;
if (process.argv.length === 1) {
    resp = 'No arguments';
} else if (process.argv.length === 2) {
    resp = 'Argument found';
} else {
    resp = 'Arguments found';
}
console.log(resp);
