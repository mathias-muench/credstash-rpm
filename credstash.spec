%global pyname credstash
%global pydesc A utility for managing secrets in the cloud using AWS KMS and DynamoDB

Name:              python-%{pyname}
Version:           1.16.1
Release:           14%{?dist}
Summary:           %{pydesc}

License:           Apache2
URL:               https://github.com/fugue/credstash
Source0:           https://github.com/fugue/%{pyname}/archive/refs/tags/v%{version}.tar.gz

BuildArch:         noarch
BuildRequires:     gcc libffi-devel openssl-devel
%if 0%{?el7}
BuildRequires:     python2-devel python2-nose python2-rpm-macros
%else
BuildRequires:     python%{python3_pkgversion}-devel python%{python3_pkgversion}-nose python3-rpm-macros
%endif

%description
%{pydesc}

%package -n python2-%{pyname}
Summary:           %{pydesc}
%{?python_provide: %python_provide python2-%{pyname}}
Requires:          python2-cryptography >= 2.1, python-boto3 >= 1.1.1
Requires(post):    %{_sbindir}/update-alternatives
Requires(postun):  %{_sbindir}/update-alternatives

%description -n python2-%{pyname}
%{pydesc}

%package -n python%{python3_pkgversion}-%{pyname}
Summary:           %{pydesc}
%{?python_provide: %python_provide python%{python3_pkgversion}-%{pyname}}
Requires:          python%{python3_pkgversion}-cryptography >= 2.1, python%{python3_pkgversion}-boto3 >= 1.1.1
Requires(post):    %{_sbindir}/update-alternatives
Requires(postun):  %{_sbindir}/update-alternatives

%description -n python%{python3_pkgversion}-%{pyname}
%{pydesc}


%prep
%autosetup -n %{pyname}-%{version}

%build
%if 0%{?el7}
%py2_build
%else
%py3_build
%endif

%install
%if 0%{?el7}
%py2_install
%{__mv} %{buildroot}/%{_bindir}/credstash.py %{buildroot}/%{_bindir}/credstash-%{python2_version}.py
%else
%py3_install
%{__mv} %{buildroot}/%{_bindir}/credstash.py %{buildroot}/%{_bindir}/credstash-%{python3_version}.py
%endif

%post -n python2-%{pyname}
%{_sbindir}/update-alternatives --install %{_bindir}/credstash %{name} %{_bindir}/credstash-%{python2_version}.py 20

%postun -n python2-%{pyname}
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/credstash-%{python2_version}.py
fi

%post -n python%{python3_pkgversion}-%{pyname}
%{_sbindir}/update-alternatives --install %{_bindir}/credstash %{name} %{_bindir}/credstash-%{python3_version}.py 30

%postun -n python%{python3_pkgversion}-%{pyname}
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/credstash-%{python3_version}.py
fi

%if 0%{?el7}
%files -n python2-%{pyname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%{_bindir}/credstash-%{python2_version}.py
%ghost %{_bindir}/credstash
%else
%files -n python%{python3_pkgversion}-%{pyname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%{_bindir}/credstash-%{python3_version}.py
%ghost %{_bindir}/credstash
%endif

%changelog
* Tue Sep 19 2023 Mathias Muench <Mathias.Muench@de.bosch.com> - 1.16.1-14
- rebuilt

