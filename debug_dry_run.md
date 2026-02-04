Last login: Wed Feb  4 12:32:24 on ttys010
tannerhochberg@Tanners-MacBook-Pro ~ % cd Desktop/ProjectFinder 
tannerhochberg@Tanners-MacBook-Pro ProjectFinder % python dry_run.py 
🚀 Starting Dry Run: Checking for projects from the last 7 days...
  👻 Setting background mode (window off-screen)...

==================================================
Scraping: City of Phoenix
==================================================
  Navigating to https://procurement.opengov.com/portal/phoenix...
  ✓ Cloudflare bypassed
  Step 2: Sorting by Release Date (newest first)...
    Checking selector: //div[@role='columnheader' and .//div[contains(text(), 'Release Date')]]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //div[contains(@class, 'rt-resizable-header-content') and text()='Release Date']
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //div[contains(@class, 'rt-th')][.//div[text()='Release Date']]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //div[@role='columnheader']//div[text()='Release Date']
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //div[contains(@class, 'rt-resizable-header-content') and contains(text(), 'Release Date')]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //th[contains(text(), 'Release')]
      - No elements found
    Checking selector: //th[contains(text(), 'release')]
      - No elements found
    Checking selector: //div[contains(@class, 'header') and contains(text(), 'Release')]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //*[contains(@class, 'sort') and contains(text(), 'Release')]
      - No elements found
    Checking selector: //button[contains(text(), 'Release Date')]
      - No elements found
    Checking selector: //*[contains(text(), 'Release Date')]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
  ⚠ Could not sort by release date, continuing anyway...
  Step 3: Triggering search...
  Step 4: Extracting projects...
  🔍 Debug: Found 'id' and 'title' in source. Check structure:
    Snippet around first 'id': "id":1913,"name":"Phoenix Municipal Court"},"status":"open","title":"Court Foreign Language Interpretation and Translation Services","isPaused":false,"isPrivate":false,"closeOutReason":null,"template":{"title":"Request For Qualification"},"copyCount":0,"id":174424,"comingSoon":false},{"releaseProjec
  ✓ Found 16 active projects

==================================================
Scraping: City of Surprise, AZ
==================================================
  Navigating to https://procurement.opengov.com/portal/surpriseaz...
  ✓ Cloudflare bypassed
  Step 2: Sorting by Release Date (newest first)...
    Checking selector: //div[@role='columnheader' and .//div[contains(text(), 'Release Date')]]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //div[contains(@class, 'rt-resizable-header-content') and text()='Release Date']
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //div[contains(@class, 'rt-th')][.//div[text()='Release Date']]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //div[@role='columnheader']//div[text()='Release Date']
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //div[contains(@class, 'rt-resizable-header-content') and contains(text(), 'Release Date')]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //th[contains(text(), 'Release')]
      - No elements found
    Checking selector: //th[contains(text(), 'release')]
      - No elements found
    Checking selector: //div[contains(@class, 'header') and contains(text(), 'Release')]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
    Checking selector: //*[contains(@class, 'sort') and contains(text(), 'Release')]
      - No elements found
    Checking selector: //button[contains(text(), 'Release Date')]
      - No elements found
    Checking selector: //*[contains(text(), 'Release Date')]
      ✓ Element 0 is displayed attempting click (Attempt 1)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 1, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 2)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 2, retrying...
      ✓ Element 0 is displayed attempting click (Attempt 3)...
      ⚠ Standard click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fb894 undetected_chromedriver + 493716
5   undetected_chromedriver             0x00000001022fb963 undetected_chromedriver + 493923
6   undetected_chromedriver             0x0000000102348880 undetected_chromedriver + 809088
7   undetected_chromedriver             0x000000010233a9f9 undetected_chromedriver + 752121
8   undetected_chromedriver             0x000000010233a3d8 undetected_chromedriver + 750552
9   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
10  undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
11  undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
12  undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
13  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
14  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
15  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
16  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
17  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
18  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
19  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
20  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
21  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15
. Trying JS click...
      ⚠ JS click failed: Message: stale element reference: stale element not found in the current frame
  (Session info: chrome=144.0.7559.133); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#staleelementreferenceexception
Stacktrace:
0   undetected_chromedriver             0x00000001028ec328 undetected_chromedriver + 6722344
1   undetected_chromedriver             0x00000001028e3b8a undetected_chromedriver + 6687626
2   undetected_chromedriver             0x00000001022f1ec5 undetected_chromedriver + 454341
3   undetected_chromedriver             0x00000001022f8f14 undetected_chromedriver + 483092
4   undetected_chromedriver             0x00000001022fbbb9 undetected_chromedriver + 494521
5   undetected_chromedriver             0x0000000102391545 undetected_chromedriver + 1107269
6   undetected_chromedriver             0x0000000102390381 undetected_chromedriver + 1102721
7   undetected_chromedriver             0x00000001023389e1 undetected_chromedriver + 743905
8   undetected_chromedriver             0x00000001023397e1 undetected_chromedriver + 747489
9   undetected_chromedriver             0x00000001028a4be1 undetected_chromedriver + 6429665
10  undetected_chromedriver             0x00000001028a8f8e undetected_chromedriver + 6446990
11  undetected_chromedriver             0x0000000102884369 undetected_chromedriver + 6296425
12  undetected_chromedriver             0x00000001028a99f8 undetected_chromedriver + 6449656
13  undetected_chromedriver             0x0000000102872a50 undetected_chromedriver + 6224464
14  undetected_chromedriver             0x00000001028cff88 undetected_chromedriver + 6606728
15  undetected_chromedriver             0x00000001028d0142 undetected_chromedriver + 6607170
16  undetected_chromedriver             0x00000001028e3791 undetected_chromedriver + 6686609
17  libsystem_pthread.dylib             0x00007ff812396e59 _pthread_start + 115
18  libsystem_pthread.dylib             0x00007ff812392857 thread_start + 15

      ⚠ Stale element on attempt 3, retrying...
  ⚠ Could not sort by release date, continuing anyway...
  Step 3: Triggering search...
  Step 4: Extracting projects...
  🔍 Debug: Found 'id' and 'title' in source. Check structure:
    Snippet around first 'id': "id":764,"name":"Parks and Recreation"},"status":"open","title":"Special Interest Classes (Continuous Selection)","isPaused":false,"isPrivate":false,"closeOutReason":null,"template":{"title":"Solicitation"},"copyCount":0,"id":9797,"comingSoon":null},{"releaseProjectDate":"2026-01-15T20:01:37.047Z","
  ✓ Found 4 active projects

🔍 Filtering for projects released after 2026-01-28...
  • Court Foreign Language Interpretation and Translat... (2026-02-04) [✓ URL]
  • HVAC Filter Maintenance and Repair... (2026-02-04) [✓ URL]
  • Automatic Transfer Switch Testing, Maintenance, an... (2026-02-04) [✓ URL]
  • Comprehensive Community Needs Assessment... (2026-02-04) [✓ URL]
  • Small Equipment Repair Services... (2026-02-04) [✓ URL]
  • Occupational Medicine Staffing Services and Electr... (2026-02-04) [✓ URL]
  • 35-65-95 Gallon Containers... (2026-02-04) [✓ URL]
  • PHOENIX SKY HARBOR INTERNATIONAL AIRPORT TERMINAL ... (2026-02-04) [✓ URL]
  • Employee Health Clinic Services... (2026-02-04) [✓ URL]
  • Lease of High-Volume Digital Color Production Pres... (2026-02-04) [✓ URL]
  • Court Foreign Language Interpretation and Translat... (2026-02-04) [✓ URL]
  • HVAC Filter Maintenance and Repair... (2026-02-04) [✓ URL]
  • Automatic Transfer Switch Testing, Maintenance, an... (2026-02-04) [✓ URL]
  • Comprehensive Community Needs Assessment... (2026-02-04) [✓ URL]
  • Small Equipment Repair Services... (2026-02-04) [✓ URL]
  • PHOENIX SKY HARBOR INTERNATIONAL AIRPORT TERMINAL ... (2026-02-04) [✓ URL]
  • Special Interest Classes (Continuous Selection)... (2026-02-04) [✓ URL]
  • Single & Dual-Purpose Police Canine (K-9) Dogs... (2026-02-04) [✓ URL]
  • Special Interest Classes (Continuous Selection)... (2026-02-04) [✓ URL]
  • Single & Dual-Purpose Police Canine (K-9) Dogs... (2026-02-04) [✓ URL]

📋 Found 20 recent projects.

📧 Sending email notification...
  📧 Sending email notification to projectfinderinfo@gmail.com...
  ✓ Email notification sent successfully!

✅ Dry run completed successfully! Check your inbox.
tannerhochberg@Tanners-MacBook-Pro ProjectFinder % 
