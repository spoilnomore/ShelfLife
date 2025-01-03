// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import BootstrapVueNext from 'bootstrap-vue-next';

import moment from 'moment';

// Add the necessary CSS
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core';

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons';

/* add icons to the library */
library.add(faUserSecret);

/* import specific icons */
import { faCat } from '@fortawesome/free-solid-svg-icons';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';
import {
    faSun,
    faMoon,
    faTrash,
    faKitchenSet,
    faSpinner,
} from '@fortawesome/free-solid-svg-icons';

import { faGoogle } from '@fortawesome/free-brands-svg-icons';

/* add icons to the library */
library.add(faCat);
library.add(faCoffee);
library.add(faSun, faMoon, faKitchenSet, faTrash, faSpinner, faGoogle);
import 'datatables.net-bs4/css/dataTables.bootstrap4.css';
import 'datatables.net-bs4';
import 'datatables.net-buttons/js/buttons.html5.js';
import 'datatables.net-buttons/js/buttons.print.js';
import 'datatables.net-buttons/js/buttons.colVis.js';

const app = createApp(App);
app.use(router);
app.use(BootstrapVueNext);
app.use(moment);
app.component('font-awesome-icon', FontAwesomeIcon);

// Set a global property for theme
app.config.globalProperties.theme = 'dark';

app.mount('#app');
