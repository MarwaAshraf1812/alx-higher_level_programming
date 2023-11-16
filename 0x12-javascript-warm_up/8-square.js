#!/usr/bin/node

const size = process.argv;
const sizeNum = parseInt(size[2]);

if (!isNaN(num) && Number.isInteger(sizeNum))
{
    for (let i = 0; i < sizeNum; i++)
    {
        let square = '';
        for (let j = 0; j < sizeNum; j++)
        {
            square += 'X';
        }
        console.log(square);
    }
}
else{
    console.log("Missing size");
}
