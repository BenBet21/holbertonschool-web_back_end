/* eslint-disable */
import Currency from './3-currency';

export default class Pricing {
  cosntructor(amount, currency) {
    if (typeof amount !== 'number')
      throw new TypeError('Amount must be a number');
    if (typeof currency !== 'currency')
      throw new TypeError('Currency must be a Currency');
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }
  set amount(value) {
    if (typeof value !== 'number')
      throw new TypeError('Amount must be a number');
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }
  set currency(value) {
    if (typeof value !== 'currency')
      throw new TypeError('Currency must be a Currency');
    this._currency = value;
  }

  displayFullPrice() {
    return `${this._amount} (${this._currency_name}) (${this._currency_code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number')
      throw new TypeError('Amount must be a number');
    if (typeof conversionRate !== 'number')
      throw new TypeError('Conversion rate must be a number');
    return amount * conversionRate;
  }
}
