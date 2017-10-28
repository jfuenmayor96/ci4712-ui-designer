// Importar css para que webpack haga el bundle
require("../css/app.scss");

// Importar dependencias JS
import Popper from 'popper.js';
import jQuery from 'jquery'

// Agregando al objeto window para que sean globales
window.jQuery = window.$ = jQuery;
window.Popper = Popper;

require("jquery-easing");
require("bootstrap");
require('./sb-admin');
