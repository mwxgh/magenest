odoo.define('test_one.bold', function (require) {
    "use strict";
    // import packages
    let basic_fields = require('web.basic_fields');
    let registry = require('web.field_registry');

    // widget implementation
    let BoldWidget = basic_fields.FieldChar.extend({
        _renderReadonly: function () {
            this._super();
            let old_html_render = this.$el.html();
            let new_html_render = '<b style="color:cyan;">' + old_html_render + '</b>'
            this.$el.html(new_html_render);
        },
    });

    registry.add('bold_cyan', BoldWidget); // add our "bold" widget to the widget registry
});