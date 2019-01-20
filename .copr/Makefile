spec=credstash.spec
outdir=$(shell rpm --eval '%{_srcrpmdir}')

srpm:
	rpmbuild --undefine=_disable_source_fetch --define='_srcrpmdir $(outdir)' -bs $(spec)

rpm:
	rpmbuild --undefine=_disable_source_fetch --define='_srcrpmdir $(outdir)' -bb $(spec)
