<template>
<div class="container">
    <div class="row my-5 card-wrapper">
        <div class="col-lg-4 col-md-6 mb-4" v-for="(vcenter, index) in vcenters" :key="index">
            <div class="card h-200">
                <div class="embed-responsive embed-responsive-16by9">
                    <img :src="image"/>
                </div>
                <div class="card-body">
                    <!-- Display vDesk Machine Name -->
                    <h4 class="card-title">
                        Machine: {{ vcenter.MachineName }}
                    </h4>
                        <template v-if="vcenter.ToolStatus === 'PoweredOn'">
                            <button type="button" 
                                    class="btn btn-danger btn-sm" 
                                    @click="DeleteMachine(vcenter)">Delete</button>

                            <button type="button" class="btn btn-danger btn-sm">Shutdown</button>
                            <button type="button" class="btn btn-danger btn-sm">Restart</button>
                        </template>

                        <template v-if="vcenter.ToolStatus === 'OffLine'">

                            <button type="button" 
                                    class="btn btn-danger btn-sm" 
                                    @click="DeleteMachine(vcenter)">Delete</button>

                            <button type="button" class="btn btn-danger btn-sm">PowerOn</button>
                        </template>

                </div>
                <div class="card-footer">
                    <small class="text-muted">
                        Machine Status: <p>{{vcenter.ToolStatus}}</p></small>
                    <br>
                    <small class="text-muted">vCenter {{vcenter.vCenter}} </small>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import image from "../assets/logo.png"

export default {
  data() {
    return {
      vcenters: [],
      image: image

    };
  },
  message:'',

methods: {
    // 1 GET METHOD
    getMachines() {
      const path = 'http://localhost:5000/vsphere';
      axios.get(path)
        .then((res) => {
          this.vcenters = res.data.vcenters;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getMachines(); 
  },
};
</script>
