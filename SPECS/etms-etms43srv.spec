Name:           etms-etms43srv
Version:        13.8.5
Release:        1%{?dist}
Summary:        eTMS etms43srv server
License:        GPL
BuildArch:      noarch

Requires:       corretto-11.0.20
Requires:       corretto-8.382
Requires:       tomcat-9.0.80
Requires:       artemis-2.28.0
Requires:       etms-reg-4.1
Requires:       etms-rep-5.3.4
Requires:       etms-app-13.8.2
Requires:       etms-dmn-13.8.2
Requires:       etms-optit

%description
eTMS etms43srv server

%prep

%install

%files

%changelog
* Tue Dec  5 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.8.2r1
* Wed Nov 29 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.7.0r1
* Tue Sep 19 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.6.1r2
* Mon Sep  4 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.6.1r1
* Thu Jul  6 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.5.0r1
* Tue Jun 13 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.4.0r1
* Thu Mar 30 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.3.0r1
* Mon Mar 20 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.2.1r2: Artemis 2.28.0
* Wed Mar 15 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.2.1r1
* Tue Jan 17 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.1.0r1
* Tue Dec 13 2022 rnyhof <rudy.nijhof@elemica.com>
- v13.0.3r1
