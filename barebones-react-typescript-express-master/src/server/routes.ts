import * as express from 'express';
import DB from '.db';

const router = express.Router();

router.get('/api/hello', (req, res, next) => {
    res.json('World');
});

router.get('/api/test', async(req,res) =>{
    try{
        let test = await DB.Test.all();
    res.json(test);
    } catch(e){
        console.log(e);
        res.sendStatus(500);
    }
    
})

export default router;