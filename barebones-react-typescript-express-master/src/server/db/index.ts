import mysql from 'mysql';
import config from '../config';

import Test from './test':

const Connection = mysql.createConnection(config.mysql);
Connection.connect(err => {
    if(err) console.log(err);
})

export default{
    Test
}