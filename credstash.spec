%global pyname credstash
%global pydesc A utility for managing secrets in the cloud using AWS KMS and DynamoDB

Name:          python-%{pyname}
Version:       1.17.1
Release:       11%{?dist}
Summary:       %{pydesc}

License:       Apache2
URL:           https://github.com/fugue/credstash
Source0:       https://github.com/fugue/%{pyname}/archive/v%{version}.tar.gz

BuildArch:     noarch
BuildRequires: gcc, libffi-devel, openssl-devel
BuildRequires: python%{python3_pkgversion}-devel, python3-rpm-macros


%description
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
%py3_build

%install
%py3_install
%{__mv} %{buildroot}/%{_bindir}/credstash.py %{buildroot}/%{_bindir}/credstash-%{python3_version}.py

%check
%{__python3} setup.py test

%post -n python%{python3_pkgversion}-%{pyname}
%{_sbindir}/update-alternatives --install %{_bindir}/credstash %{name} %{_bindir}/credstash-%{python3_version}.py 30

%postun -n python%{python3_pkgversion}-%{pyname}
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/credstash-%{python3_version}.py
fi

%files -n python%{python3_pkgversion}-%{pyname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%{_bindir}/credstash-%{python3_version}.py
%ghost %{_bindir}/credstash

%changelog
