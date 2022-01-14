<template>
<div class="col-12 col-md-10 col-lg-7">
    <div class="list-group list-group-flush">
       <div class="list-group-item d-flex align-items-start" v-for="(appointment, index) in appointments" :key="index">
           <button class="mr-2 btn btn-sm btn-danger" @click="$emit('remove', appointment)"><font-awesome-icon icon="trash"/></button>
           <div class="w-100">
               <div class="d-flex justify-content-between">
                   <span class="h4 text-primary" contenteditable="contenteditable"
                         @blur="$emit('edit', appointment.id, 'petName', $event.target.innerText)">
                          {{appointment.petName}}
                    </span>
                   <span class="float-right">{{appointment.aptDate}}</span>
                </div>
                <div class="owner-name">
                    <span class="font-weight-bold text-primary mr-1">Owner:</span>
                    <span contenteditable="contenteditable"
                         @blur="$emit('edit', appointment.id, 'petOwner', $event.target.innerText)">
                         {{appointment.petOwner}}
                    </span>
                </div>
                <div>{{appointment.aptNote}}</div>
            </div>
        </div>
    </div>
</div>
</template>
<script>

import  {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
export default {
    name: "AppointmentList",
    props: ["appointments"],
    components: {
        FontAwesomeIcon
  }
};
</script>
