import { createStore } from "vuex";
import axios from "axios"


export default createStore({
  state: {
    vdesks: [],
    SearchvDesks: [],
    PostTitle: '',
  },
  
  getter: {
    TitleUser: state => {
      return state.PostTitle;
    },
    vdesk: state => {
      return state.PostTitlevDesk;
    },
    TitleDesk: state => {
      return state.Click;
    }
  },
  
  mutations: {
  SET_VDESKS(state, payload){
    state.vdesks = payload;
  },

  SET_USERVDESKS(state, payload){
    state.SearchvDesks = payload;
},

  PostTitle(state, payload) {
    state.PostTitle = payload;
 },
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
        (commit("SET_USERVDESKS", res.data.SearchvDesks))  
    })
    .catch((error) => {
        console.error(error);
    });
  },

 async postData({commit, state}, data) {
  const path = 'http://localhost:5000/powercycle';
  const result = await axios.post(path,
    { TitleUser: state.PostTitle, data });
    axios.get('http://localhost:5000/horizon')
    .then((res) => {
        (commit("SET_VDESKS", res.data.vdesks))
    })
    .catch((error) => {
        console.error(error)
    });
  return result
 }
},
  modules: {},
});
