# Credstash RPM

Early version, tested roughly with Fedora Core 29

## Build RPM using rpmbuild

    rpmbuild --undefine=_disable_source_fetch -bb credstash.spec

## Build RPM using mock

    mock -r epel-7-x86_64 --rebuild --nocheck /home/muenchm/rpmbuild/SRPMS/python-credstash-1.14.0-9.fc29.src.rpm

> CAUTION: EL7 seems not to have a boto3 library for python3, so python3 package will not be installable on EL
