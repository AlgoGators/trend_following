# trend-following
Using formula's provided by Carver in chapters 5-9, we create a multiple trend following strategy that returns a forecast.

$
N_(i,t) = Capped combined forecast \cdot Capital \cdot IDM \cdot Weight_i \cdot \tau \div (10 \cdot Multiplier_i \cdot Price_(i,t) \cdot FX_(i,t) \cdot \sigma_(\%,i,t))
$
