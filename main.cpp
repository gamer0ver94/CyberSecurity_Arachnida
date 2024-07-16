#include <curl/curl.h>
#include <iostream>
int main(int argc, char** argv)
{
    if (argc < 2)
        return -1;
    CURL *curl = curl_easy_init();
  if(curl) {
    CURLcode res;
    curl_easy_setopt(curl, CURLOPT_URL, argv[1]);
    res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
  }
    return 0;
}