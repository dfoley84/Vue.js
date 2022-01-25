<template>
  <div class="container" style=" padding-top: 50px;">
     <!-- Bootswatch -->
 
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
                <button type="button" 
                        class="btn btn-outline-warning"
                        @click="postData({'vSphere':'Horizon','PowerCycle':'PowerOff', 'vDesk':vdesk})">
                        <i class="fas fa-power-off"></i></button>

                 <button type="button" 
                         class="btn btn-outline-primary" 
                         @click="postData({'vSphere':'Horizon','PowerCycle':'Restart', 'vDesk':vdesk})">
                         <i class="fas fa-recycle"></i></button>

                 <button type="button" 
                         class="btn btn-outline-danger"
                         @click="postData({'vSphere':'Horizon','PowerCycle':'Delete', 'vDesk':vdesk})">
                         <i class="fas fa-trash"></i></button>
  
              <template v-if="vdesk.MachineOpt == 'Windows'">
                   <button type="button"
                           class="btn btn-outline-info">
                           <i class="fas fa-desktop"></i></button>
              </template>
              </template>

              <template v-if="vdesk.MachineStatus == 'Powered Off'">
                <button type="button" 
                         class="btn btn-outline-danger"
                         @click="postData({'vSphere':'Horizon','PowerCycle':'Delete', 'vDesk':vdesk})">
                         <i class="fas fa-power-off"></i></button>
      
                <button type="button" 
                         class="btn btn-outline-danger"
                         @click="postData({'vSphere':'Horizon','PowerCycle':'Delete', 'vDesk':vdesk})">
                         <i class="fas fa-trash"></i></button>
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
  </div>
</template>

<script>

//TO-DO Move SubmitPowerCycle to VUEX 
import Spinner from '@/components/Spinner.vue';
import {mapState, mapActions} from 'vuex';

export default {
data() {
    return {
      polling: null,  
    };
	},
  
message: '',

computed:{
  ...mapState(['vdesks']),
},

components: {
    Spinner
},

methods: {
    ...mapActions(['postData']),


  pollData () {
    this.polling = setInterval (() => {
      this.$store.dispatch("FeatchvDesks")
    }, 12000)
  }
},

beforeUnmount() {
  clearInterval(this.polling)
},

created() {
    this.$store.dispatch("FeatchvDesks")
    this.pollData()
  },
};
</script>
