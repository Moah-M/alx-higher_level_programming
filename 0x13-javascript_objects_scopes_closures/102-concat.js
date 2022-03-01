#!/usr/bin/node

const frs = require('fs');
const dt1 = frs.readFileSync(process.argv[2], 'utf-8');
const dt2 = frs.readFileSync(process.argv[3], 'utf-8');
frs.writeFileSync(process.argv[4], dt1 + dt2, 'utf-8');
