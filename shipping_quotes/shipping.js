function domesticQuote(parcel) {
  const volumetricWeight = (parcel.lengthCm * parcel.widthCm * parcel.heightCm) / 5000;
  const chargeableWeight = Math.max(parcel.weightKg, volumetricWeight);
  let price = 4.5 + chargeableWeight * 1.2;
  if (parcel.fragile) {
    price += 3;
  }
  return Math.round(price * 100) / 100;
}

function internationalQuote(parcel) {
  const volumetricWeight = (parcel.lengthCm * parcel.widthCm * parcel.heightCm) / 5000;
  const chargeableWeight = Math.max(parcel.weightKg, volumetricWeight);
  let price = 12 + chargeableWeight * 3.8;
  if (parcel.fragile) {
    price += 3;
  }
  return Math.round(price * 100) / 100;
}

module.exports = { domesticQuote, internationalQuote };
