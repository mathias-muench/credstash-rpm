%global pyname credstash
%global sum A little utility for managing credentials in the cloud

Name:          python-%{pyname}
Version:       1.15.0
Release:       10%{?dist}
Summary:       %{sum}

License:       Apache2
URL:           https://github.com/fugue/credstash
Source0:       https://github.com/fugue/%{pyname}/archive/v%{version}.tar.gz

BuildArch:     noarch
BuildRequires: gcc libffi-devel openssl-devel
BuildRequires: python2-devel python2-nose python2-rpm-macros
BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}-nose python3-rpm-macros


%description
A utility for managing secrets in the cloud using AWS KMS and DynamoDB


%package -n python2-%{pyname}
Summary:       %{sum}
%{?python_provide: %python_provide python2-%{pyname}}
Requires:      python2-cryptography >= 2.1, python-boto3 >= 1.1.1, python-botocore, python-futures

%description -n python2-%{pyname}
A utility for managing secrets in the cloud using AWS KMS and DynamoDB


%package -n python%{python3_pkgversion}-%{pyname}
Summary:       %{sum}
%{?python_provide: %python_provide python%{python3_pkgversion}-%{pyname}}
Requires:      python%{python3_pkgversion}-cryptography >= 2.1, python%{python3_pkgversion}-boto3 >= 1.1.1, python%{python3_pkgversion}-botocore

%description -n python%{python3_pkgversion}-%{pyname}
A utility for managing secrets in the cloud using AWS KMS and DynamoDB


%prep
%autosetup -n %{pyname}-%{version}

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
# If, however, we're installing separate executables for python2 and python3,
# the order needs to be reversed so the unversioned executable is the python2 one.
%py2_install
%py3_install

#%check
#%{__python2} setup.py test
#%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{pyname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{pyname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%{_bindir}/*

%changelog
