Polymer('ex-dialog',{
    open: function(){
        this.$.overlay.open();
    },
    toggle: function(){
        this.$.overlay.toggle();
    },
    getDialogContent: function(){
        return this.$.dc.shadowRoot;
    }
});