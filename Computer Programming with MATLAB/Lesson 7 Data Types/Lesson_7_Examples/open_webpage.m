function open_webpage
url = input('Enter the url: ','s');
if isempty(url)
    fprintf("No url entered, so quitting.\n");
    return;
end
search_time = datetime; % same as datetime("now")
status = web(url);
if status == 0 % started web browser
    fprintf("At %s, you opened the web page at\n",search_time);
fprintf("%s\n",url);
else
    fprint("Could not start web browser\n");
end
[~,weekday_name] = weekday(search_time,'long');
fprintf("Have a great %s!\n", weekday_name);
