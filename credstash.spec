%global pyname credstash
%global pydesc A utility for managing secrets in the cloud using AWS KMS and DynamoDB

Name:          python-%{pyname}
Version:       1.15.0
Release:       11%{?dist}
Summary:       %{pydesc}

License:       Apache2
URL:           https://github.com/fugue/credstash
Source0:       https://github.com/fugue/%{pyname}/archive/v%{version}.tar.gz

BuildArch:     noarch
BuildRequires: gcc libffi-devel openssl-devel
BuildRequires: python2-devel python2-nose python2-rpm-macros
BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}-nose python3-rpm-macros


%description
%{pydesc}


%package -n python2-%{pyname}
Summary:       %{pydesc}
%{?python_provide: %python_provide python2-%{pyname}}
Requires:      python2-cryptography >= 2.1, python-boto3 >= 1.1.1
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description -n python2-%{pyname}
%{pydesc}


%package -n python%{python3_pkgversion}-%{pyname}
Summary:       %{pydesc}
%{?python_provide: %python_provide python%{python3_pkgversion}-%{pyname}}
Requires:      python%{python3_pkgversion}-cryptography >= 2.1, python%{python3_pkgversion}-boto3 >= 1.1.1
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description -n python%{python3_pkgversion}-%{pyname}
%{pydesc}


%prep
%autosetup -n %{pyname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%{__mv} %{buildroot}/%{_bindir}/credstash.py %{buildroot}/%{_bindir}/credstash-%{python2_version}.py
%py3_install
%{__mv} %{buildroot}/%{_bindir}/credstash.py %{buildroot}/%{_bindir}/credstash-%{python3_version}.py

#%check
#%{__python2} setup.py test
#%{__python3} setup.py test

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

%if 0%{?fedora} >= 28
%files -n python2-%{pyname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%{_bindir}/credstash-%{python2_version}.py
%ghost %{_bindir}/credstash

%files -n python%{python3_pkgversion}-%{pyname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%{_bindir}/credstash-%{python3_version}.py
%ghost %{_bindir}/credstash
%endif

%changelog
