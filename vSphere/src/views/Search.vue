<template>

<div class="container" style="padding-top: 50px;">
<div class="row">
<div class="col-lg-4 col-md-4 col-sm-6 col-sm-offset-4 col-xs-6 col-xs-offset-4 ">
  <div class="form-group">
    <label for="FormUserName">Enter Username</label>
    <input v-model="TitleUser" type="text" class="form-control" id="FormUserName" placeholder="Enter Username">
  </div>
  <div class="form-group">
   <button class="btn btn-primary col-12 my-4" @click="SubmitForm">Submit</button>
  </div>
</div>
</div>

<div class="row my-5 card-wrapper">
      <div
			class="col-lg-4 col-md-6 mb-4"
			v-for="(vdesk, index) in SearchvDesks"
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
  </div>
</template>

<script>
import Spinner from '@/components/Spinner.vue';
import {mapState} from 'vuex';

export default {
    data() {
        return {
            polling: null,
        }
    },
    message: '',
    components: {
    Spinner,
    
},
computed: {
  ...mapState(['SearchvDesks']),
  
  TitleUser: {
    set(TitleUser) {
      this.$store.commit('PostTitle', TitleUser);
    },
  },
},

methods: {
   SubmitForm() {
     this.$store.dispatch('FetchUservDesks', this.payload);
  },
  
  pollData() {
    this.polling = setInterval(() => {
      this.$store.dispatch('FetchUservDesks', this.payload)
    },120000)
  }
},

beforeUnmount() {
  clearInterval(this.polling)
},

created() {
  this.pollData()
  },
  
};
</script>
