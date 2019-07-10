function cal_str = make_calendar(n_month,n_year)
% MAKE_CALENDAR(MONTH,YEAR) one-month calendar with month-year heading
%  CALENDAR = MAKE_CALENDAR(...) CALENDAR is a column of strings

dt = datetime(n_year,n_month,1); % 3rd arg, day, is arbitrary
dt.Format = 'MMMM yyyy'; % format of calendar's title
title_str = string(dt);  % calendar's title
cal_num = calendar(dt);  % days of the month in a double array
cal_str = strings(11,1); % pre-allocation
left = blanks(floor(14-strlength(title_str)/2)); % padding to center title
right = blanks(ceil(14-strlength(title_str)/2)); % padding to center title
cal_str([1,3,11]) = " -------------------------- "; % decoration
cal_str(2) = sprintf('%s',left,title_str,right); % centered title
cal_str(4) = " Su  Mo  Tu  We  Th  Fr  Sa ";     % day-of-week headings
for ii = 1:6 % loops through rows of cal_num
    temp = sprintf("%3s ",string(cal_num(ii,:)));
    cal_str(ii+4) = strrep(temp," 0","  "); % replaces 0 with blank
end

