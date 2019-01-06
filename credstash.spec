Name: credstash
Version: 1.14.0
Release: 7
Summary: A little utility for managing credentials in the cloud

License: Apache License 2.0
URL: https://github.com/fugue/credstash
Source0: https://github.com/fugue/%{name}/archive/v%{version}.tar.gz

BuildArch: noarch
BuildRequires: gcc libffi-devel python-devel openssl-devel python-setuptools
Requires: python2-cryptography >= 1.5
Requires: python2-cryptography < 2.1
Requires: python-boto3 >= 1.1.1
Requires: python-botocore >= 1.5.0
Requires: python-futures >= 2.2.0


%description
A little utility for managing credentials in the cloud

%prep
%setup -n %{name}-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%check
%{__python2} setup.py test


%files
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%{_bindir}/*

%changelog
