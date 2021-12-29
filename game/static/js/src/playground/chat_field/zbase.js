class ChatField {
    constructor(playground) {
        this.playground = playground;

        this.$history = $(`<div class="ac-game-chat-field-history"></div>`);
        this.$input = $(`<input type="text" class="ac-game-chat-field-input">`);

        this.$history.hide();
        this.$input.hide();
        this.playground.$playground.append(this.$history);
        this.playground.$playground.append(this.$input);

        this.start();
    }
    start() {
        this.add_listening_events();
    }
    add_listening_events() {
        let outer = this;
        this.$input.keydown(function(e) {
            if (e.which === 27) {
                outer.hide_input();
                return false;
            }
        });
    }
    show_input() {
        this.$input.show();
        this.$input.focus();
    }
    hide_input() {
        this.$input.hide();
        this.playground.game_map.$canvas.focus();
    }
}