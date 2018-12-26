import {createStore, combineReducers, applyMiddleware} from "redux";
import thunk from "redux-thunk";
import users from "redux/modules/users";

const env =process.env.NODE_ENV;
            //node js 의 정보

const middlewares = [thunk];

if(env==='development'){
    const {logger} = require('redux-logger');
    middlewares.push(logger);
}

const reducer = combineReducers({
    users,
});

let store = initialState => createStore(reducer, applyMiddleware(...middlewares));
                                                             //[1,2,3]->(1,2,3) unpack
export default store();