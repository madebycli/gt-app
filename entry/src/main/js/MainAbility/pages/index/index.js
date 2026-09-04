export default {
  data: {
    status: 'GT6 TEST READY',
    count: 0
  },

  onShow() {
    console.info('GT6 Test page visible');
  },

  clickAction() {
    this.count += 1;
    this.status = this.count === 1 ? 'TOUCH OK' : 'GT6 TEST OK';
    console.info(`GT6 Test tap count: ${this.count}`);
  }
};
