<template>
  <div class="container">
    <div class="row my-5 card-wrapper">
      <div
        class="col-lg-4 col-md-6 mb-4"
        v-for="(vcenter, index) in vcenters"
        :key="index">
        
        <div class="card h-200">
          <div class="embed-responsive embed-responsive-16by9">

            <!-- Display Image -->
            <template v-if="vcenter.MachineOpt === 'Mint'">
                <div class="text-center">
                    <img v-bind:src="require('../assets/mint.png')" />
                </div>
            </template>

            <template v-if="vcenter.MachineOpt === 'Ubuntu'">
                <div class="text-center">
                    <img v-bind:src="require('../assets/ubuntu.png')" />
                </div>
            </template>

            <template v-if="vcenter.MachineOpt === 'Windows'">
                <div class="text-center">
                    <img v-bind:src="require('../assets/windows.png')" />
                </div>
            </template>            
          </div>

          <!-- Card Body -->
          <div class="card-body">
              <v-card-title>
                  <v-row align="center" class="mx-0">
                      <div class="grey--text ms-4">
                          Machine Name: {{vcenter.MachineName}}
                      </div>
                  </v-row>
              </v-card-title>

              <v-divider class="mx-4"></v-divider>

             <!--Display for vSphere Machines Powered On-->
            <template v-if="vcenter.ToolStatus === 'PoweredOn'">
                <div class="text-center">
                    <v-btn class="mx-2" fab dark small color="primary" @click="StopMachine(vcenter)">
                        <v-icon dark> mdi-stop </v-icon>
                    </v-btn>

                     <v-btn class="mx-2" fab dark small color="primary" @click="deleteMachine(vcenter)">
                        <v-icon dark> mdi-delete </v-icon>
                    </v-btn>

                    <v-btn class="mx-2" fab dark small color="primary" @click="StopMachine(vcenter)">
                        <v-icon dark> mdi-restart </v-icon>
                    </v-btn>
                    
                    <template v-if="vcenter.MachineOpt === 'Windows'">
                    <v-btn class="mx-2" fab dark small color="primary" @click="ConnectMachine(vcenter)">
                        <v-icon dark> mdi-remote</v-icon>
                    </v-btn>
                    </template>
                </div>
            </template>
            

            <!--Display for vSphere Machines Powered Off-->
            <template v-if="vcenter.ToolStatus === 'OffLine'">
              <div class="text-center">
                    <v-btn class="mx-2" fab dark small color="primary" @click="StartMachine(vcenter)">
                        <v-icon dark> mdi-play </v-icon>
                    </v-btn>

                     <v-btn class="mx-2" fab dark small color="primary" @click="deleteMachine(vcenter)">
                        <v-icon dark> mdi-delete </v-icon>
                    </v-btn>
              </div>
            </template>
            <!--Display for vSphere Machines Running Cycle Job-->
            <template v-if="vcenter.ToolStatus === 'RunningJob'">
              <Spinner />
            </template>
          </div>

          <!-- Card Footer -->
          <div class="card-footer">
              <v-card-text>
                  <v-row align="center" class="mx-0">
                       Machine Status: {{vcenter.ToolStatus}}
                  </v-row>
                <div class="my-4 text-subtitle-1">
               
                </div>
            </v-card-text>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import Spinner from "@/components/Spinner.vue";

export default {
  data() {
    return {
      vcenters: [],
    };
  },
  message: "",

  components: {
    Spinner,
  },

  methods: {
    // GET vCenter METHOD
    machinename() {
      const path = "http://localhost:5000/vsphere";
      axios
        .get(path)
        .then((res) => {
          this.vcenters = res.data.vcenters;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // Remove vCenter METHOD
    RemoveMachine(machinename) {
        const path = `http://localhost:5000/vsphere/${machinename}`;
        axios.delete(path)
        .then(() => {
            this.machinename();
            this.message = 'vSphere Machine Has been Set to Delete 🗑️!';
            this.showMessage = true;
        })
        .catch((error) => {
            console.error(error);
            this.machinename();
        });
    },
    // Handle Delete Button
    deleteMachine(game) {
        this.RemoveMachine(game.id);
    },
  },
  created() {
    this.getvcenters();
  },
};
</script>
