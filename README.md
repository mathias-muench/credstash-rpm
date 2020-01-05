# Credstash RPM

A RPM package for [fugue/credstash: A little utility for managing credentials in the cloud](https://github.com/fugue/credstash).

In use since Fedora Core 29 and CentOS7 since some years.

## Build 

Using `rpmbuild`: `make -f .copr/Makefile rpm`

Using `mock`: `make -f .copr/Makefile root=epel-7-x86_64 mock`

Prebuilt packages are availablable in [mmu/credstash-rpm Copr](https://copr.fedorainfracloud.org/coprs/mmu/credstash-rpm/).

## Install

Fedora: `dnf install python3-credstash`.

CentOS7: `yum install python2-credstash`.

Python2/3 versions may be installed in parallel, binary can be chosen via `alternatives(8)`.
