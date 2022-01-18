import { createStore } from "vuex";
import axios from "axios"

export default createStore({
  state: {
    vdesks: []
  },
  mutations: {
    SET_VDESKS(state, payload){
      state.vdesks = payload;
  }
},
  actions: {
    fetchVdesk({commit}){
      const path = 'http://localhost:5000/horizon';
      axios.get(path)
      .then((res) => {
          (commit("SET_VDESKS", res.data.vdesks))
      })
      .catch((error) => {
          console.error(error)
      });
  }
  },
  


  modules: {},
});
