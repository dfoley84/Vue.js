import { createStore } from "vuex";
import axios from "axios"


export default createStore({
  state: {
    vdesks: [],
    PostTitle: '',
  },
  
  getter: {
    TitleUser: state => {
      return state.PostTitle;
    }
  },
  
  mutations: {
    SET_VDESKS(state, payload){
      state.vdesks = payload;
  },
  PostTitle(state, newtitle) {
    state.PostTitle = newtitle;
 }
},
  actions: {
    FeatchvDesks({commit}){
      const path = 'http://localhost:5000/horizon';
      axios.get(path)
      .then((res) => {
          (commit("SET_VDESKS", res.data.vdesks))
      })
      .catch((error) => {
          console.error(error)
      });
  },
  
  FetchUservDesks({commit, state}) {
    const path = 'http://localhost:5000/searchdata';
    axios.post(path, {
      TitleUser: state.PostTitle
  })
    .then((res) => {
        (commit("SET_VDESKS", res.data.vdesks))  
    })
    .catch((error) => {
        console.error(error);
    });
  },
},
  
  modules: {},
});
