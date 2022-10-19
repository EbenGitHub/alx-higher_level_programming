#!/usr/bin/node

//File input and output
//using fs module (file system)
//it reads it from oprating system (it needs the help of the operating system)
//There are two ways of doing it: sync and async

//Let us begin//

//Import the fs module
const fs = require('fs');


//........READ FILE............

//Prepare our read options
let read_options = {
	encoding: 'utf-8',
	flag: 'r'
};

//read the file
fs.readFile('file.txt', read_options, (err, data) => {
	console.log(data.toString());
});




//........WRITE FILE............

//Prepare our write options
let write_options {
	encoding: 'utf-8',
	flag: 'w',
	mode: 0o666
};

//write the file
fs.writeFile('file.txt', 'hello world', write_options, err => {

	if (err) {
		// do something with error
	}
});




//...........DELETE FILE.........
fs.unlink('file.txt', err => {
	if (err) {
		// do something with error
	}
});
