Polymer({
    onResponse: function(event) {
        this.shadowRoot.innerHTML = event.detail.response;
    }
});