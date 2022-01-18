<template>
<div class="container">
<div class="row">

<form @submit.prevent="SubmitForm" method="post">
    <input type="text" v-model="posts.username" placeholder="Username">
    <button type="submit">Submit</button>
</form>

<div class="row my-5 card-wrapper">
      <div
			class="col-lg-4 col-md-6 mb-4"
			v-for="(vdesk, index) in vdesks"
			:key="index">
        <div class="card h-200">
            <div class="embed-responsive embed-responsive-16by9">
				<!-- Display Image -->
				<template v-if="vdesk.MachineOpt == 'Windows'">
					<div class="text-center">
						<img v-bind:src="require('@/assets/windows.png')" />
					</div>
				</template>
				<template v-if="vdesk.MachineOpt == 'Ubuntu'">
					<div class="text-center">
					    <img v-bind:src="require('@/assets/linux.png')" />
					</div>
			    </template>

          <div class="card-body">
                <!-- Display vDesk Machine Name -->
                <h4 class="card-title">
                    vDesk: {{ vdesk.MachineName }}
                </h4>
              <!-- Display vDesk Status -->
              <p class="card-text">Machine State: {{ vdesk.MachineStatus }}</p>

              <!-- Action Buttons -->
              <template v-if="vdesk.MachineStatus != 'Powered Off' && vdesk.MachineStatus != 'Running Job'">
                 <button type="button" class="btn btn-outline-warning"><i class="fas fa-power-off"></i></button>
                 <button type="button" class="btn btn-outline-primary"><i class="fas fa-recycle"></i></button>
                 <button type="button" class="btn btn-outline-danger"><i class="fas fa-trash"></i></button>
  
              <template v-if="vdesk.MachineOpt == 'Windows'">
                   <button type="button" class="btn btn-outline-info"><i class="fas fa-desktop"></i></button>
              </template>
              </template>

              <template v-if="vdesk.MachineStatus == 'Powered Off'">
                <button ><i class="fas fa-power-off"></i> Start </button>
                <button btn btn-info ><i class="fas fa-trash"></i> Delete </button>
              </template>

              <template v-if="vdesk.MachineStatus == 'Running Job'">
                <Spinner />
              </template>
              
                <!-- Footer -->
               <div class="card-footer" style="margin-top: 5px;">
                 <small small-class="text-muted" >
                   Desktop Pool: {{ vdesk.vPool }}
                 </small>
                 <br>
                   <small small-class="text-muted" >
                   Horizon Server: {{ vdesk.vCenter }}
                 </small>
               </div>
		      </div>
        </div>
      </div>
          <!-- End of Card --> 
    </div>
  </div>
    <!-- Pager Footer -->
    <Footer />
  </div>
</div>
</template>

<script>
import axios from 'axios'
import Spinner from '@/components/Spinner.vue';
import Footer from '@/components/Footer.vue';

export default {
    data() {
        return {
            vdesks:[],
            polling: null,
            posts:{
                username: '',
            }
        }
    },
    message: '',
    components: {
    Spinner,
    Footer
},
    methods: {
        SubmitForm() {
            const path = 'http://localhost:5000/searchdata';
            axios.post(path,this.posts)
            .then((res) => {
                this.vdesks = res.data.vdesks;  
            })
            .catch((error) => {
                console.error(error);
            });
        },
    pollData() {
    this.polling = setInterval (() => {
      this.SubmitForm()
    }, 120000)
  }
},
beforeUnmount() {
  this.pollData()
},
created() {
  this.pollData()
  },
};
</script>

