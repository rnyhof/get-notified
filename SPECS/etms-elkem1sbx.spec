Name:           etms-elkem1sbx
Version:        13.10.7
Release:        1%{?dist}
Summary:        eTMS elkem1sbx webapp & daemon
License:        GPL
BuildArch:      noarch

Requires:       corretto-11
Requires:       tomcat-9
Requires:       artemis-2.28.0
Requires:       etms-reg-4.1
Requires:       etms-rep-5.3.4
Requires:       etms-optit
Requires:       etms-app-%{version}
Requires:       etms-dmn-%{version}

%description
eTMS elkem1sbx webapp & daemon

%prep

%install

%files

%changelog
* Tue Feb 13 2024 rnyhof <rudy.nijhof@elemica.com>
- v13.10.1r1
* Tue Jan  9 2024 rnyhof <rudy.nijhof@elemica.com>
- v13.9.0r1
* Thu Nov 23 2023 whaan<wim.dehaan@elemica.com>
- v13.8.1r1
* Thu Nov  2 2023 whaan <wim.dehaan@elemica.com>
- v13.8.0r1
* Wed Oct 11 2023 whaan <wim.dehaan@elemica.com>
- v13.7.0r1
* Wed Sep  6 2023 whaan <wim.dehaan@elemica.com>
- v13.6.1r1
* Wed Jul 12 2023 whaan <wim.dehaan@elemica.com>
- v13.5.0r1
* Tue May  9 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.4.0r1
* Thu Mar 23 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.2.1r2: Update Artemis to 2.28.0.
* Thu Mar 16 2023 rnyhof <rudy.nijhof@elemica.com>
- v13.2.1r1
