#!/usr/bin/node
/*
Remove the first two elements
*/ 
const arguments = process.argv.slice(2);

if (arguments.some((arg, index) => index in arguments)) {
    arguments.forEach((arg, index) => {
    	
    });
}
else
{
    console.log('No argument');
}
if (arguments.length >= 2)
{
    const input1 = arguments[0];
    const input2 = arguments[1];
    console.log(input1, 'is', input2);
}
