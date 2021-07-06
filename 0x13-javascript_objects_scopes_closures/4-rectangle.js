#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a;
    let b;
    let ShowRect = '';
    for (a = 0; a < this.height; a++) {
      if (a > 0) {
        ShowRect += '\n';
      }
      for (b = 0; b < this.width; b++) {
        ShowRect += 'X';
      }
    }
    console.log(ShowRect);
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const swp = this.height;
    this.height = this.width;
    this.width = swp;
  }
}

module.exports = Rectangle;
