#!/usr/bin/node
const arguments = process.argv.slice(2);

const numArguments = arguments.length;

if (numArguments === 0)
{
    console.log('No arguments');
}
else if (numArguments === 1)
{
    console.log('Argument found');
}
else
{
    console.log('Arguments found');
}
    
    
