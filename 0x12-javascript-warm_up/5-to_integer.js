#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2]);

/*!isNaN(num) ensures that parseInt successfully 
parsed a number before checking if it's an integer*/

if (!isNaN(num) && Number.isInteger(num))
{
    console.log('My number:' + args[2]);
}
else{
    console.log('Not a number');
}
