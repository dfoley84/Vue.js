<template>
  <div id="main-app" class="container">
    <div class="row justify-content-center">
      <appointment-list :appointments="appointments" @remove="deletePet" @edit="editPet" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import _ from "lodash";
import AppointmentList from '../src/components/AppointmentList.vue'

export default {
  data() {
    return {
      appointments: [],
       AppointmentForm: {
          id: '',
          petName: '',
          petOwner: '',
          aptDate: '',
          aptNote: ''
      }
    };
  },
  components: {
    AppointmentList
  },

methods: {
    // GET PETS 
    getAppointments() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.appointments = res.data.appointments;
        })
        .catch((error) => {
          console.error(error);
        });
    }, //Exit GetAppointments
    //Server Call
    intervalFetchData: function () {
            setInterval(() => {    
                this.getAppointments();
                }, 60000);    
        }, // Exit FecthData
    //Remove Pet Function
    removePet(petName) {
      const path = `http://localhost:5000/${petName}`;
      axios.delete(path)
      .then(() => {
        this.getAppointments();
        })
        .catch((error) => {
          console.error(error);
          this.getAppointments();
          });
      },
      // Handle Delete Button
    deletePet(appointments) {
      this.removePet(appointments.petName);
    },//End Remove Pet

    // Append Pet  (Working Front-End not Passing to backEnd -> need to Fix)
  updatePet(petName) {
    const path = `http://localhost:5000/${petName}`;
    axios.put(path)    
    .then(() => {
      this.getAppointments();
    })
    .catch((error) => {
      console.error(error);
      this.getAppointments();
    });
},
 // Handle Update Button 
editPet(appointments, field, text) {
  const index = _.findIndex(this.appointments, {
    PetID : appointments.petName
  });
  this.appointments[index][field] = text;
  this.updatePet(appointments.petName);
},
    }, //Exit Methods
  created() {
    this.getAppointments(); 
    this.intervalFetchData();
  },
};
</script>
