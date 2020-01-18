Name: openoffice.org-dict-cs_CZ
Version: 20060303
Release: 14%{?dist}
Summary: Czech spellchecker and hyphenation dictionaries for OpenOffice.org
License: GPL+
Group: Applications/Productivity
URL: ftp://ftp.linux.cz/pub/localization/OpenOffice.org/devel/Czech/spell_checking/
Source0: openoffice.org-dict-cs_CZ.tar.gz
BuildArch: noarch

%define hunspelldir %{_datadir}/myspell
%define hyphendir %{_datadir}/hyphen

%description
This package contains the czech hyphenation dictionaries for the Openoffice.org
application suite.

%package -n hunspell-cs
Group: Applications/Text
Summary: Czech hunspell dictionary
Requires: hunspell
Obsoletes: openoffice.org-dict-cs_CZ < %{version}-%{release}

%description -n hunspell-cs
This package contains the czech dictionary for the hunspell spellchecker.

%package -n hyphen-cs
Group: Applications/Text
Summary: Czech hyphenation rules
Requires: hyphen
Obsoletes: openoffice.org-dict-cs_CZ < %{version}-%{release}

%description -n hyphen-cs
Czech hyphenation rules.

%prep
%setup -q -n %{name}

%build
iconv -f ISO-8859-2 -t UTF-8 README_hyph_cs_CZ.txt > README_hyph_cs_CZ.txt.new
mv -f README_hyph_cs_CZ.txt.new README_hyph_cs_CZ.txt

%install
mkdir -p $RPM_BUILD_ROOT%{hunspelldir}
install -m 644 cs* $RPM_BUILD_ROOT%{hunspelldir}
mkdir -p $RPM_BUILD_ROOT%{hyphendir}
install -m 644 hyph*.dic $RPM_BUILD_ROOT%{hyphendir}

%files -n hyphen-cs
%doc README_hyph_cs_CZ.txt
%{hyphendir}/hyph_cs*

%files -n hunspell-cs
%doc README_cs_CZ.txt
%{hunspelldir}/cs*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20060303-14
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 26 2007 Tomas Mraz <tmraz@redhat.com> - 20060303-7
- add obsoletes openoffice.org-dict-cs_CZ

* Mon Nov 26 2007 Caolan McNamara <caolanm@redhat.com> - 20060303-6
- Resolves: rhbz#398361 move hyphenation rules into hyphen dir where OOo will now autodetect them

* Tue Mar 27 2007 Tomas Mraz <tmraz@redhat.com> - 20060303-5
- add hunspell-cs subpackage (#232416)
- openoffice datadir moved again

* Mon Jan 29 2007 Tomas Mraz <tmraz@redhat.com> - 20060303-4
- disable useless debuginfo (#225094)

* Mon Dec 11 2006 Tomas Mraz <tmraz@redhat.com> - 20060303-3
- package must be arch-specific now because ooo is now 64bit on x86_64 as
  well (#219100)

* Thu Sep  7 2006 Tomas Mraz <tmraz@redhat.com> - 20060303-2
- rebuilt for FC6

* Tue Mar 21 2005 Tomas Mraz <tmraz@redhat.com> - 20060303-1
- Initial package
