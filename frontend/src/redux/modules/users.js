//import

//actions

//action creators

//initial state
const initialState ={
    isLoggedIn: localStorage.getItem('jwt') || false
}

//reducer

function reducer(state=initialState, action){
    switch(action.type){
        default:
            return state;
    }
}

//reducer functions

//export action creators

//export reducer
export default reducer;