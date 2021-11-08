class AcGamePlayground {
    constructor(root) {
        this.root = root;
        this.$playground = $(`<div>游戏界面</div>`);
        this.hide();
        this.root.$ac_game.append(this.$playground);
        this.start();
    }
    
    start() {
    }
    
    show() { // 打开playground界面
        this.$playground.show();
    }
    
    hide() { // 关闭playground界面
        this.$playground.hide();
    }
}