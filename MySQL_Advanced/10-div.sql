-- 10-div.sql
function safe_divide(a INT, b INT) {
	if (b == 0) {
		return 0;
	}
	return a / b;
}
